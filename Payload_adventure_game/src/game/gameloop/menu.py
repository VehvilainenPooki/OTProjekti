import os

import pygame

dirname = os.path.dirname(__file__)

class Menu():

    def __init__(self, clock, screen):
        self.clock = clock
        self.screen = screen
        pygame.mouse.set_visible(True)

        self.start_button = pygame.sprite.Sprite()

        self.start_button.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "menu", "startbg.png")
        )

        self.start_button.image = pygame.transform.scale(
            self.start_button.image, (22*10, 10*10))

        self.start_button.rect = pygame.Rect((100, 100), (100,100))


    def mainmenu_screen(self):
        running = True
        while running:
            # Exit event
            running = self._is_running()

            self.screen.blit(self.start_button.image, self.start_button.rect)

            pygame.display.update()
            self.clock.tick(60)



    def _is_running(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return False
        return True


