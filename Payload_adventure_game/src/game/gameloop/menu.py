import os

import pygame

from ..entities.menu.menuButton import MenuButton

dirname = os.path.dirname(__file__)

class Menu():

    def __init__(self, clock, screen):
        self.clock = clock
        self.screen = screen
        pygame.mouse.set_visible(True)

        self.cooldown = 0
        self.bright = False

        self.start_button = MenuButton(os.path.join(dirname, "..", "assets", "menu", "start.png"), "Start", 100, 100, 10)

        self.settings_button = MenuButton(os.path.join(dirname, "..", "assets", "menu", "settings.png"), "Settings", 100, 300, 10)

        self.mainmenu_buttons = pygame.sprite.Group()
        self.mainmenu_buttons.add(
            self.start_button,
            self.settings_button
        )

        self.settingsmenu_buttons = pygame.sprite.Group()

        self.under_mouse_buttons = pygame.sprite.Group()


    def mainmenu_screen(self):
        running = True
        while running:
            # Exit event
            running = self._is_running()

            action = self._update_mouse()
            if action == "Start":
                return "Start"
            self._draw(self.mainmenu_buttons)

            pygame.display.update()
            self.clock.tick(60)



    def _is_running(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return False
        return True
    
    def _update_mouse(self):
        pos = pygame.mouse.get_pos()
        pygame.event.get()
        pressed = pygame.mouse.get_pressed(3)[0]

        self._mouse_collision(pos)

        if pressed:
            return self._interact_with_mouse()
        

    def _draw(self, group):
        for button in group:
            self.screen.blit(button.get_image(), button.get_rect())

    def _mouse_collision(self, pos):
        for button in self.under_mouse_buttons:
            if not button.rect.collidepoint(pos):
                button.pointer_is_off()
                self.under_mouse_buttons.remove(button)

        for button in self.mainmenu_buttons:
            if not self.under_mouse_buttons.has(button):
                if button.rect.collidepoint(pos):
                    button.pointer_is_on()
                    self.under_mouse_buttons.add(button)

    def _interact_with_mouse(self):
        group = self.under_mouse_buttons.sprites()
        if len(group) == 1:
            return group[0].button_action()
        return "F"
