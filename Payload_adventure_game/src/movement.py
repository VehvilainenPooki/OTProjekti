import pygame
from player import Player

class Movement:

    def __init__(self, p):
        self.player = p
        self.dash_x = 0
        self.dash_y = 0
        self.dash_cooldown = 0
    
    def move(self):
        #print("in movement")
        keys = pygame.key.get_pressed()

        
        #Activating dash
        if keys[pygame.K_SPACE] and self.dash_cooldown < 1:
            x = 0
            y = 0
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
        
        #Checking if player is sprinting
        if keys[pygame.K_LSHIFT]:
            speed = 7
        elif keys[pygame.K_LCTRL]:
            speed = 3
        else:
            speed = 5
        
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
        