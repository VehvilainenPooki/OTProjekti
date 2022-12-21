import os

import pygame

from game.world.chunkloader import ChunkLoader
from game.logic.movement import Movement
from game.logic.collisions import Collisions

from game.rendering.camera import Camera

dirname = os.path.dirname(__file__)

class Adventure():

    def gameloop(self, clock, screen, resolution):
        pygame.mouse.set_visible(False)

        background = pygame.Surface(resolution)
        background.fill((50,100,50))

        # Loading first chunk
        chunkloader = ChunkLoader(1)
        chunkloader.all_sprites.draw(screen)

        # Initializing movement
        player = chunkloader.get_player()
        pointer = chunkloader.get_pointer()
        movement = Movement(player, pointer)
        # Initializing camera
        cam = Camera(player, resolution)

        # Initializing collision detection
        collisions = Collisions(player)
        
        # Main loop for now
        print("\nLaunching Payload_adventure_game.\nPressing [esc] closes the game")
        running = True
        while running:
            # Exit event
            running = self._is_running()

            # moving player
            movement.move()

            # Checking circle collision
            for sprite in chunkloader.ground_sprites:
                if collisions.are_colliding(player, sprite):
                    collisions.remove_collision(player, sprite)

            # Drawing frame
            screen.blit(background, (0, 0))
            cam_offset = cam.get_pos()
            for sprite in chunkloader.all_sprites:
                s_pos = sprite.get_rendering_pos()
                screen.blit(sprite.image, (s_pos[0] -
                            cam_offset[0], s_pos[1]-cam_offset[1]))

            screen.blit(pointer.image, pointer.rect)

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
    -menu
    -settings
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