import pygame
import os

dirname = os.path.dirname(__file__)

class TerrainSprite(pygame.sprite.Sprite):
    posx = 0
    posy = 0
    hboxr = 0

    def __init__(self, x=0, y=0, r=20):
        self.posx = x
        self.posy = y
        self.hboxr = r

        super().__init__()
        
        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "trees", "tree1.png")
        )
       
        self.image = pygame.transform.scale(self.image, (self.hboxr*2,self.hboxr*2))
        self.rect = pygame.Rect((self.posx, self.posy),(self.hboxr*2,self.hboxr*2))


    
    def get_pos(self):
        return (self.posx, self.posy)
    
    def get_hitbox_r(self):
        return self.hboxr
    
    