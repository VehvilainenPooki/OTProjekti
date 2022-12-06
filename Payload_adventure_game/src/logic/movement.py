import math
import pygame

class Movement:

    def __init__(self, game_player):
        self.player = game_player
        self.dash_x = 0
        self.dash_y = 0
        self.dash_cooldown = 0

    def move(self):
        #print("in movement")
        keys = pygame.key.get_pressed()


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

    def remove_collision(self, circle):
        #Checking how much to move the player
        p_pos = self.player.rect.center
        c_pos = circle.rect.center
        dist_p_c = math.dist(p_pos, c_pos)
        c_radius = circle.get_hitbox_r()
        p_c_overlap = (self.player.get_hitbox_r()+c_radius)-dist_p_c

        dist_x = math.dist([p_pos[0]], [c_pos[0]])
        dist_y = math.dist([p_pos[1]], [c_pos[1]])
        if dist_p_c == 0:
            return
        dist_x = dist_x*(p_c_overlap/dist_p_c)
        dist_y = dist_y*(p_c_overlap/dist_p_c)
        #Checking which direction to move the player
        if p_pos[0] < c_pos[0]:
            dist_x = -dist_x
        if p_pos[1] < c_pos[1]:
            dist_y = -dist_y

        #Moving the player
        self.player.add_pos(dist_x, dist_y)
