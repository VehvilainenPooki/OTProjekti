import pygame

from .player import Player
from .terrainsprite import TerrainSprite



class ChunkLoader:
    def __init__(self, level_map):
        self.player = None
        self.terrainsprites = pygame.sprite.Group()
        #tbd rocks
        self.ground_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def _initialize_sprites(self, level_map):
        self.player = Player(100, 100, 50, 20)
        self.terrainsprites.add(TerrainSprite(400,-260, 50))
        self.terrainsprites.add(TerrainSprite(400,200, 50))
        self.terrainsprites.add(TerrainSprite(700,100,50))


        self.ground_sprites.add(
            self.terrainsprites
            #tbd rocks
        )

        self.all_sprites.add(
            self.player,
            self.ground_sprites
        )

    def get_player(self):
        return self.player