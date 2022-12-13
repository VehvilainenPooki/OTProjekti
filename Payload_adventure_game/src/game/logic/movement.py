import math
import pygame

class Movement:
    """Handles Player movement
    """

    def __init__(self, game_player):
        self.player = game_player
        self.dash_x = 0
        self.dash_y = 0
        self.dash_cooldown = 0

    def move(self):
        keys = pygame.key.get_pressed()

        self.dash(keys)

        
        self.take_a_step(keys, self.movement_speed(keys))

    def movement_speed(self, keys):
        if keys[pygame.K_LSHIFT]:
            return 7
        elif keys[pygame.K_LCTRL]:
            return 3
        else:
            return 5

    def take_a_step(self, keys, speed):
        if keys[pygame.K_w]:
            #print("w")
            self.player.add_pos(0,-speed)
        if keys[pygame.K_s]:
            #print("s")
            self.player.add_pos(0,speed)
        if keys[pygame.K_d]:
            #print("d")
            self.player.add_pos(speed,0)
        if keys[pygame.K_a]:
            #print("a")
            self.player.add_pos(-speed,0)


    def dash(self, keys):
        #Activating dash
        if keys[pygame.K_SPACE] and self.dash_cooldown < 1:
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
        #Moving player while dashing
        if self.dash_cooldown > 0:
            if self.dash_cooldown > 30:
                self.player.add_pos(10*self.dash_x,10*self.dash_y)
            self.dash_cooldown -= 1
