import pygame
from sys import exit

from chunkloader import ChunkLoader
from movement import Movement
from camera import Camera
from Collisions import Collisions


def main():
    #Initialising window
    resolution = (1920, 1080)
    pygame.init()
    screen = pygame.display.set_mode(resolution, pygame.NOFRAME)
    pygame.display.set_caption("Playload_adventure_game")
    clock = pygame.time.Clock()
    
    background = pygame.Surface(resolution)

    #Loading first chunk
    chunkloader = ChunkLoader(1)
    chunkloader.all_sprites.draw(screen)

    #Initializing movement
    player = chunkloader.get_player()
    movement = Movement(player)
    #Initializing camera
    c = Camera(player, resolution)

    #Initializing collision detection
    collisions = Collisions(player)
    # Main loop for now
    print("\nLaunching Payload_adventure_game.\nPressing [esc] closes the game")
    running = True
    while running:
        # Exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
                exit()
        1

        #moving player
        movement.move()

        #Checking circle collision
        for sprite in chunkloader.all_sprites:
            if collisions.are_colliding(sprite):
                movement.remove_collision(sprite)
        
        #Drawing frame
        screen.blit(background, (0, 0))
        for sprite in chunkloader.all_sprites:
            screen.blit(sprite.image, (sprite.rect.x - c.get_x(), sprite.rect.y - c.get_y()))

        pygame.display.update()
        clock.tick(60)


    pygame.quit()

if __name__ == "__main__":
    main()