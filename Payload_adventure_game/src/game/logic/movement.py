import os
import math

import pygame


dirname = os.path.dirname(__file__)


class Movement:
    """Movement handles Player and mouse movement

    Attributes:
        game_player: the player object of the game
        mouse_pointer: the pointer object of the game
    """

    def __init__(self, game_player, mouse_pointer=None):
        """Classes constructor which creates a new Movement object for the arguments.

        Args:
            game_player (Player): Gets the Player object
            mouse_pointer (Pointer): Gets the pointer object
        """
        self.player = game_player
        self.pointer = mouse_pointer
        self.dash_x = 0
        self.dash_y = 0
        self.dash_cooldown = 0

    def move(self, resolution):
        """Method to move player and pointer
        """
        keys = pygame.key.get_pressed()

        self._dash(keys)

        self._take_a_step(keys, self._movement_speed(keys))

        if self.pointer is not None:
            self._update_pointer_pos()
            self._look_at_pointer(resolution)

    def _movement_speed(self, keys):
        """Gets the movement speed option which is currently pressed

        Args:
            keys (key.get_pressed()): All keys current activation status

        Returns:
            speed (int): Returns the speed at which to move the player
        """
        if keys[pygame.K_LSHIFT]:
            return 7
        if keys[pygame.K_LCTRL]:
            return 3
        return 5

    def _take_a_step(self, keys, speed):
        """Moves the player a step in users held direction with the speed multiplier.

        Args:
            keys (key.get_pressed()): All keys current activation status
            speed (int): The step distance multiplier
        """
        if keys[pygame.K_w]:
            self.player.add_pos(0, -speed)
        if keys[pygame.K_s]:
            self.player.add_pos(0, speed)
        if keys[pygame.K_d]:
            self.player.add_pos(speed, 0)
        if keys[pygame.K_a]:
            self.player.add_pos(-speed, 0)

    def _dash(self, keys):
        """Moves the player quickly in a direction for a short amout of time.
        Dash is active for 10 frames and then has 30 frame cooldown.

        Args:
            keys (key.get_pressed()): All keys current activation status
        """
        # Activating dash
        if keys[pygame.K_SPACE] and self.dash_cooldown < 1:
            self._activate_dash(keys)

        # Moving player while dashing
        if self.dash_cooldown > 0:
            if self.dash_cooldown > 30:
                self.player.add_pos(10*self.dash_x, 10*self.dash_y)
            self.dash_cooldown -= 1

    def _activate_dash(self, keys):
        """Checking if no cooldown
        and then reading user inputs for the dash direction.

        Args:
            keys (key.get_pressed()): All keys current activation status
        """
        if keys[pygame.K_w] and keys[pygame.K_s] == 0:
            self.dash_y = -1
        elif keys[pygame.K_s] and keys[pygame.K_w] == 0:
            self.dash_y = 1
        else:
            self.dash_y = 0
        if keys[pygame.K_a] and keys[pygame.K_d] == 0:
            self.dash_x = -1
        elif keys[pygame.K_d] and keys[pygame.K_a] == 0:
            self.dash_x = 1
        else:
            self.dash_x = 0
        if self.dash_x == 0 and self.dash_y == 0:
            self.dash_y = -1
        self.dash_cooldown = 40

    def _update_pointer_pos(self):
        """Updates mouse pointer position.
        """
        self.pointer.spin()

    def _look_at_pointer(self, resolution):
        """Rotates player model to look at the mouse pointer.
        """
        po_pos = self.pointer.get_pos()

        pl_angle = math.atan2(
            resolution[0]/2-po_pos[0], resolution[1]/2-po_pos[1])*(180/math.pi)

        self.player.image = pygame.transform.scale(
            self.player.get_original_image(), (self.player.hitbox_radius*2, self.player.hitbox_radius*2)) #pylint: disable=line-too-long

        self.player.image = pygame.transform.rotate(
            self.player.image, pl_angle)
