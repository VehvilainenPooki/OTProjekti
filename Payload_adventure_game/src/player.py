
import pygame
import os


dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, r = 10, h = 20):
        
        super() .__init__()

        self.posx = x
        self.posy = y
        self.hboxr = r
        self.health = h
        
        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "player", "player.png")
        )

        self.image = pygame.transform.scale(self.image, (self.hboxr*2,self.hboxr*2))

        self.rect = pygame.Rect((self.posx, self.posy),(self.hboxr*2,self.hboxr*2))


    
    def get_pos(self):
        return (self.posx, self.posy)
    
    def set_pos(self, x, y):
        self.posx = x
        self.posy = y
    
    def get_hitbox_r(self):
        return self.hboxr
    