import os

import pygame

from logic.chunkloader import ChunkLoader
from logic.movement import Movement
from logic.collisions import Collisions

from rendering.camera import Camera

dirname = os.path.dirname(__file__)

def main():
    #Initialising window
    resolution = (1920, 1080)
    pygame.init()
    screen = pygame.display.set_mode(resolution, pygame.NOFRAME)
    pygame.display.set_caption("Playload_adventure_game")
    clock = pygame.time.Clock()

    pygame.mouse.set_visible(False)

    background = pygame.Surface(resolution)

    #Loading first chunk
    chunkloader = ChunkLoader(1)
    chunkloader.all_sprites.draw(screen)

    #Initializing movement
    player = chunkloader.get_player()
    movement = Movement(player)
    #Initializing camera
    cam = Camera(player, resolution)

    #Initializing collision detection
    collisions = Collisions(player)
    # Main loop for now
    print("\nLaunching Payload_adventure_game.\nPressing [esc] closes the game")
    pointer_angle = 0
    running = True
    while running:
        # Exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        #moving player
        movement.move()

        #Checking circle collision
        for sprite in chunkloader.ground_sprites:
            if collisions.are_colliding(sprite):
                movement.remove_collision(sprite)


        m_pos = pygame.mouse.get_pos()
        pointer = pygame.sprite.Sprite()
        pointer.image = pygame.image.load(
            os.path.join(dirname, "assets", "mouse", "pointer.png")
        )
        pointer.image = pygame.transform.scale(pointer.image, (32,32))

        #pointer.rect = pygame.Rect((self.posx, self.posy),(self.hboxr*2,self.hboxr*2))
        pointer.rect = pointer.image.get_rect()
        pointer.image = pygame.transform.rotate(pointer.image, pointer_angle)
        pointer_angle -= 1
        i_size = pointer.image.get_rect().center
        pointer.rect = (m_pos[0]-i_size[0],m_pos[1]-i_size[1])


        #Drawing frame
        screen.blit(background, (0, 0))
        cam_offset = cam.get_pos()
        for sprite in chunkloader.all_sprites:
            screen.blit(sprite.image, (sprite.rect.x-cam_offset[0], sprite.rect.y-cam_offset[1]))


        screen.blit(pointer.image, pointer.rect)



        pygame.display.update()
        clock.tick(60)


    pygame.quit()

if __name__ == "__main__":
    main()
