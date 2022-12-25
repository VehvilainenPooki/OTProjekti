import unittest

import pygame

from game.world.chunkloader import ChunkLoader

from game.entities.terrain_sprite import TerrainSprite
from game.entities.player import Player



class TestChunkloader(unittest.TestCase):
    def test_chunkloader_init(self):
        ChunkLoader("test")

    def test_loads(self):
        self.loader = ChunkLoader("test")
        
        terrainsprites = pygame.sprite.Group()
        terrainsprites.add(
            TerrainSprite(200,0, 60, 200, 2),
            TerrainSprite(-100, 250, 30, 200, 1),
            TerrainSprite(300,-200, 60, 200, 1),
            TerrainSprite(-300, -350, 60, 200, 1),
            TerrainSprite(450, 400, 60, 200, 1),
            TerrainSprite(-500, 550, 60, 200, 1),
            TerrainSprite(650,-600, 60, 200, 1),
            TerrainSprite(-700,-750, 60, 200, 1),
            TerrainSprite(-850, 800, 60, 200, 2),
            TerrainSprite(900, 950, 60, 200, 2),
            TerrainSprite(-1050, -1000, 60, 200, 2),
            TerrainSprite(1100, -1150, 60, 200, 2),
            TerrainSprite(-1250, 1200, 60, 200, 2),
            TerrainSprite(1300,1350, 60, 200, 2)
        )

        ground_sprites = pygame.sprite.Group()
        ground_sprites.add(
            terrainsprites
        )

        all_sprites = pygame.sprite.Group()
        all_sprites.add(
            Player(100,100,50,20),
            ground_sprites
        )
        
        all_same = True
        for i in range(len(all_sprites)):
            if type(self.loader.all_sprites.sprites()[i]) is not type(all_sprites.sprites()[i]):
                all_same = False
                break

        self.assertEqual(all_same, True)

    def test_loader_player_get(self):
        self.loader = ChunkLoader("test")

        self.assertEqual(type(Player(100,100,50,20)) == type(self.loader.get_player()), True)
