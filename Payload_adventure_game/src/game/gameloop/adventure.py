import os

import pygame

from game.world.chunkloader import ChunkLoader

from game.logic.movement import Movement
from game.logic.collisions import Collisions

from game.rendering.camera import Camera

dirname = os.path.dirname(__file__)


class Adventure():

    def __init__(self, renderer):
        self.renderer = renderer

        self.chunkloader = ChunkLoader(1)

        self.player = self.chunkloader.get_player()
        self.pointer = self.chunkloader.get_pointer()
        self.movement = Movement(self.player, self.pointer)

        self.collisions = Collisions(self.player)

        self.cam = Camera(self.player)
        self.renderer.set_camera(self.cam)

    def gameloop(self, clock, screen, scale, resolution):
        self.renderer.update_scaling(resolution, scale)
        print(
            "\nLaunching Payload_adventure_game.\nPressing [esc] closes the game")
        running = True
        while running:
            running = self._is_running()

            pygame.mouse.set_visible(False)

            self.movement.move(resolution)

            for sprite in self.chunkloader.ground_sprites:
                if self.collisions.are_colliding(self.player, sprite):
                    self.collisions.remove_collision(self.player, sprite)

            self.renderer.render_frame(screen, self.chunkloader.all_sprites)

            screen.blit(self.pointer.image, self.pointer.rect)

            pygame.display.update()
            clock.tick(60)

    def _is_running(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.__dict__.get("key") == 27 and event.type == 768):
                return False
        return True


"""Todo:
- create index.py and clean up this mess
- ui
    -menu x
    -settings x
    -pause menu
- resolution scaling
- mobs
    -ai
    -textures
    attack
    -taking damage
- player
    -attack
    -taking damage
- payload
    -movement
    -damage
    -interaction
"""
