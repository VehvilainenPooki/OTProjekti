import pygame

from ..entities.player import Player
from ..entities.pointer import Pointer

from ..entities.terrainsprite import TerrainSprite


class ChunkLoader:
    """Class to load in the environment chunk by chunk
    At this time it just load in the test env.
    """

    def __init__(self, level_map):
        """Classes constructor which creates a ChunkLoader

        Args:
            level_map (map): todo: map files that can be loaded at the start to init the world.
        """
        self.player = None
        self.pointer = Pointer()
        self.terrainsprites = pygame.sprite.Group()
        # tbd rocks
        self.ground_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def _initialize_sprites(self, level_map):
        """Loads in the sprites to the world

        Args:
            level_map (map): todo: map files that can be loaded at the start to init the world.
        """
        self.player = Player(100, 100, 50, 20)
        self.terrainsprites.add(TerrainSprite(400, -260, 50))
        self.terrainsprites.add(TerrainSprite(400, 200, 50))
        self.terrainsprites.add(TerrainSprite(700, 100, 50))

        self.ground_sprites.add(
            self.terrainsprites
            #todo: rocks
        )

        self.all_sprites.add(
            self.player,
            self.ground_sprites
        )

    def get_player(self):
        return self.player

    def get_pointer(self):
        return self.pointer
