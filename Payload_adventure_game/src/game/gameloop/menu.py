import os

import pygame

from game.entities.menu.menu_button import MenuButton
from game.entities.menu.text_sprite import TextSprite

dirname = os.path.dirname(__file__)


class Menu():

    def __init__(self, clock, screen, scale, resolution):
        """Menu gameloop class constructor

        Args:
            clock (pygame.clock): The games clock
            screen (pygame.display): The games screen
            scale (int): The games current scaling value
            resolution (tuple): The games current resolution (width,height)
        """
        self.clock = clock
        self.screen = screen
        self.last_frame_mouse_pressed = False

        self.scale = scale
        self.resolution = resolution

        self.new_resolution = self.resolution

        self.background = pygame.Surface(resolution)
        self.background.fill((50, 50, 50))

        self._init_mainmenu()
        self._init_settingsmenu(resolution)

    def _init_mainmenu(self):
        self.start_button = MenuButton(
            os.path.join(dirname, "..", "assets", "menu", "start.png"), "Start", self.resolution[0]/20, self.resolution[1]/10, 10) #pylint: disable=line-too-long
        self.settings_button = MenuButton(
            os.path.join(dirname, "..", "assets", "menu", "settings.png"), "Settings", self.resolution[0]/20, 2*(self.resolution[1]/10), 10) #pylint: disable=line-too-long
        self.quit_button = MenuButton(
            os.path.join(dirname, "..", "assets", "menu", "quit.png"), "Quit", self.resolution[0]/20, self.resolution[1]-2*(self.resolution[1]/10), 10) #pylint: disable=line-too-long

        self.mainmenu_buttons = pygame.sprite.Group()
        self.mainmenu_buttons.add(
            self.start_button,
            self.settings_button,
            self.quit_button
        )

    def _init_settingsmenu(self, resolution):
        self.resolution_button = MenuButton(
            os.path.join(dirname, "..", "assets", "menu", "resolution.png"), "Resolution", self.resolution[0]/20, 1*(self.resolution[1]/10), 10) #pylint: disable=line-too-long
        self.resolution_text = TextSprite(
            str(resolution[0])+"x"+str(resolution[1]), None, 6*(self.resolution[0]/20), 1*(self.resolution[1]/10), 10) #pylint: disable=line-too-long
        self.apply_button = MenuButton(
            os.path.join(dirname, "..", "assets", "menu", "apply.png"), "Apply", self.resolution[0]/20, 2*(self.resolution[1]/10), 10) #pylint: disable=line-too-long
        self.back_button = MenuButton(
            os.path.join(dirname, "..", "assets", "menu", "back.png"), "Back", self.resolution[0]/20, self.resolution[1]-2*(self.resolution[1]/10), 10) #pylint: disable=line-too-long

        self.settingsmenu_buttons = pygame.sprite.Group()
        self.settingsmenu_buttons.add(
            self.resolution_button,
            self.resolution_text,
            self.apply_button,
            self.back_button
        )

        self.under_mouse_buttons = pygame.sprite.Group()

    def mainmenu_screen(self, resolution, scale):
        """Method tha starts the mainmenu screen loop.

        Args:
            resolution (tuple): The games current resolution (width,height)
            scale (int): The games current scaling value

        Returns:
            str: Action that the menu wants to do
        """
        self._use_current_scaling(resolution, scale)
        running = True
        while running:
            running = self._is_running()

            action = self._update_mouse(self.mainmenu_buttons)
            if action is not None:
                return action
            self._draw(self.mainmenu_buttons)

            pygame.display.update()
            self.clock.tick(60)
        return "Quit"

    def settingsmenu_screen(self, resolution, scale):
        """Method that starts the settingsmenu screen loop.

        Args:
            resolution (tuple): The games current resolution (width,height)
            scale (int): The games current scaling value

        Returns:
            str: Action that the menu wants to do
        """
        self._use_current_scaling(resolution, scale)
        running = True
        while running:
            running = self._is_running()

            action = self._update_mouse(self.settingsmenu_buttons)
            if action is not None:
                if action == "Back":
                    return ("Back")  # pylint: disable=superfluous-parens
                if action == "Apply":
                    self.resolution = self.new_resolution
                    return ("Apply", self.resolution)
                if action == "Resolution":
                    self._change_resolution_text()
            self._draw(self.settingsmenu_buttons)

            pygame.display.update()
            self.clock.tick(60)

    def _is_running(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.__dict__.get("key") == 27 and event.type == 768):
                return False
        return True

    def _update_mouse(self, menu):
        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed(3)[0]

        self._mouse_collision(pos, menu)

        if not pressed:
            self.last_frame_mouse_pressed = False
            return None
        if not self.last_frame_mouse_pressed:
            self.last_frame_mouse_pressed = True
            return self._interact_with_mouse()
        return None

    def _draw(self, group):
        self.screen.blit(self.background, (0, 0))
        for button in group:
            self.screen.blit(button.get_image(), button.get_rect())

    def _mouse_collision(self, pos, menu):
        for button in self.under_mouse_buttons:
            if not menu.has(button):
                button.pointer_is_off()
                self.under_mouse_buttons.remove(button)
            elif not button.rect.collidepoint(pos):
                button.pointer_is_off()
                self.under_mouse_buttons.remove(button)

        for button in menu:
            if not self.under_mouse_buttons.has(button):
                if button.rect.collidepoint(pos):
                    button.pointer_is_on()
                    self.under_mouse_buttons.add(button)

    def _interact_with_mouse(self):
        group = self.under_mouse_buttons.sprites()
        if len(group) == 1:
            return group[0].button_action()
        return None

    def _change_resolution_text(self):
        if self.new_resolution == (1280, 720):
            self.new_resolution = (1920, 1080)
            self.resolution_text.change_text("1920x1080")
            return
        if self.new_resolution == (1920, 1080):
            self.new_resolution = (2560, 1440)
            self.resolution_text.change_text("2560x1440")
            return
        if self.new_resolution == (2560, 1440):
            self.new_resolution = (3840, 2160)
            self.resolution_text.change_text("3840x2160")
            return
        self.new_resolution = (1280, 720)
        self.resolution_text.change_text("1280x720")

    def _use_current_scaling(self, resolution, scale):
        self.resolution = resolution
        self.scale = scale

        self.background = pygame.Surface(self.resolution)
        self.background.fill((50, 50, 50))

        self.start_button.change_pos_scale(
            self.resolution[0]/20, 2*(self.resolution[1]/10), self.scale)
        self.settings_button.change_pos_scale(
            self.resolution[0]/20, 4*(self.resolution[1]/10), self.scale)
        self.quit_button.change_pos_scale(
            self.resolution[0]/20, self.resolution[1]-2*(self.resolution[1]/10), self.scale)

        self.resolution_button.change_pos_scale(
            self.resolution[0]/20, 2*(self.resolution[1]/10), self.scale)
        self.resolution_text.change_pos_scale(
            self.resolution[0]/3, 2*(self.resolution[1]/10), self.scale)
        self.apply_button.change_pos_scale(
            self.resolution[0]/20, 4*(self.resolution[1]/10), self.scale)
        self.back_button.change_pos_scale(
            self.resolution[0]/20, self.resolution[1]-2*(self.resolution[1]/10), self.scale)
