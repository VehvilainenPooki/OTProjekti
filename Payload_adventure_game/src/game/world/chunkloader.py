import os

import pygame

from ..entities.player import Player
from ..entities.pointer import Pointer

from ..entities.terrain_sprite import TerrainSprite

dirname = os.path.dirname(__file__)


class ChunkLoader:
    """Class to load in the environment chunk by chunk

    Attributes:
        level_map (int): Tells which level to load
    """

    def __init__(self, level_map):
        """Classes constructor which creates a ChunkLoader

        Args:
            level_map (int): Tells which level to load
        """
        self.player = None
        self.pointer = Pointer()
        self.terrainsprites = pygame.sprite.Group()
        self.ground_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.initialize_level(level_map)

    def initialize_level(self, level_map):
        """Loads in the selected level

        Args:
            level_map (int): Tells which level to load
        """

        start_zone_location = os.path.join(
            dirname, "levels", "level_"+str(level_map), "zone1.txt")

        self.load_zone(start_zone_location)

        self.ground_sprites.add(
            self.terrainsprites
        )

        self.all_sprites.add(
            self.player,
            self.ground_sprites
        )

    def load_zone(self, location):
        zone = open(location, "r")
        for zone_part in zone:
            if len(zone_part) < 4:
                continue
            parts = zone_part.split(" ")
            if parts[0] == "Player":
                self._init_player(parts)
                continue
            if parts[0] == "Tree":
                self._init_tree(parts)
        zone.close()

    def _init_player(self, data):
        pos = data[1].split(",")
        self.player = Player(int(pos[0]), int(pos[1]), 50, 20)

    def _init_tree(self, data):
        pos = data[1].split(",")
        if int(data[2]) == 1:
            self.terrainsprites.add(TerrainSprite(
                int(pos[0]), int(pos[1]), 30, 200, 1))
            return
        if int(data[2]) == 2:
            self.terrainsprites.add(TerrainSprite(
                int(pos[0]), int(pos[1]), 60, 200, 2))
            return

    def get_player(self):
        return self.player

    def get_pointer(self):
        return self.pointer
