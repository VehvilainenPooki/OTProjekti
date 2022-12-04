import pygame
from sys import exit

from chunkloader import ChunkLoader
from movement import Movement


def main():
    #Initialising window
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Playload_adventure_game")
    clock = pygame.time.Clock()

    background = pygame.Surface((800, 400))

    #Loading first chunk
    chunkloader = ChunkLoader(1)
    chunkloader.all_sprites.draw(screen)

    #Initializing movement
    movement = Movement(chunkloader.get_player())

    # Main loop for now
    running = True
    while running:
        # Exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        1

        #move player
        #print("Going into movement")
        movement.move()
        # Moving camera/player



        # Rendering frame
        screen.blit(background, (0, 0))

        chunkloader.all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(60)


    pygame.quit()

if __name__ == "__main__":
    main()