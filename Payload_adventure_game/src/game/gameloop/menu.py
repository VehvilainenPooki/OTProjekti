import os

import pygame

from ..entities.menu.menuButton import MenuButton

dirname = os.path.dirname(__file__)

class Menu():

    def __init__(self, clock, screen):
        self.clock = clock
        self.screen = screen
        self.last_frame_mouse_pressed = False

        self.cooldown = 0
        self.bright = False

        self.background = pygame.Surface((1920, 1080))
        self.background.fill((50,50,50))

        self.start_button = MenuButton(os.path.join(dirname, "..", "assets", "menu", "start.png"), "Start", 100, 100, 10)
        self.settings_button = MenuButton(os.path.join(dirname, "..", "assets", "menu", "settings.png"), "Settings", 100, 300, 10)
        self.quit_button = MenuButton(os.path.join(dirname, "..", "assets", "menu", "quit.png"), "Quit", 100, 1000, 10)

        self.mainmenu_buttons = pygame.sprite.Group()
        self.mainmenu_buttons.add(
            self.start_button,
            self.settings_button,
            self.quit_button
        )



        self.resolution_button = MenuButton(os.path.join(dirname, "..", "assets", "menu", "resolution.png"), "Resolution", 100, 100, 10)
        self.apply_button = MenuButton(os.path.join(dirname, "..", "assets", "menu", "apply.png"), "Apply", 100, 300, 10)
        self.back_button = MenuButton(os.path.join(dirname, "..", "assets", "menu", "back.png"), "Back", 100, 600, 10)

        self.settingsmenu_buttons = pygame.sprite.Group()

        self.settingsmenu_buttons.add(
            self.resolution_button,
            self.apply_button,
            self.back_button
        )

        self.under_mouse_buttons = pygame.sprite.Group()


    def mainmenu_screen(self):
        running = True
        while running:
            running = self._is_running()

            action = self._update_mouse(self.mainmenu_buttons)
            if type(action) != type(None):
                print("mainmenu action: " + action)
                return action
            self._draw(self.mainmenu_buttons)

            pygame.display.update()
            self.clock.tick(60)
        return "Quit"

    def settingsmenu_screen(self):
        running = True
        while running:
            running = self._is_running()

            action = self._update_mouse(self.settingsmenu_buttons)
            if action == "Back":
                print("leaving settings")
                return
            self._draw(self.settingsmenu_buttons)

            pygame.display.update()
            self.clock.tick(60)



    def _is_running(self):
        for event in pygame.event.get():
            print(event, event.type)
            if event.type == pygame.QUIT or (event.__dict__.get("key") == 27 and event.type == 768):
                return False
        return True
    
    def _update_mouse(self, menu):
        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed(3)[0]

        self._mouse_collision(pos, menu)

        if not pressed:
            self.last_frame_mouse_pressed = False
            return
        if not self.last_frame_mouse_pressed:
            self.last_frame_mouse_pressed = True
            return self._interact_with_mouse()
        

    def _draw(self, group):
        self.screen.blit(self.background, (0,0))
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
        return
