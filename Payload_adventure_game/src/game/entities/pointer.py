import os

import pygame


dirname = os.path.dirname(__file__)


class Pointer(pygame.sprite.Sprite):
    """Class that gives the mouse pointer a custom appearence

    Args:
        pygame (Sprite): pygame Sprite Super
    """

    def __init__(self):
        """Classes constructor which creates a Pointer
        """
        super() .__init__()

        self.pointer_angle = 0

        self.original_image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "mouse", "pointer.png")
        )

        self.image = pygame.transform.scale(self.original_image, (32, 32))

        self.rect = self.image.get_rect()

    def spin(self):
        """Method that spins the pointer image and moves the pointer to the mouse location.
        """
        m_pos = pygame.mouse.get_pos()

        self.image = pygame.transform.scale(self.original_image, (32, 32))

        self.image = pygame.transform.rotate(self.image, self.pointer_angle)
        self.pointer_angle -= 1

        i_size = self.image.get_rect().center
        self.rect = (m_pos[0]-i_size[0], m_pos[1]-i_size[1])

    def get_pos(self):
        i_size = self.image.get_rect().center
        pos = (self.rect[0]+i_size[0], self.rect[1]+i_size[1])
        return pos

    def get_rendering_pos(self):
        i_size = self.image.get_rect().center
        pos = (self.rect[0]-i_size[0], self.rect[1]-i_size[1])
        return pos
