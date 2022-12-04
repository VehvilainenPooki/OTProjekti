import pygame
from sys import exit

from chunkloader import ChunkLoader



def main():
    #Initialising window
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Playload_adventure_game")
    clock = pygame.time.Clock()

    background = pygame.Surface((800, 400))

    chunkloader = ChunkLoader(1)
    
    chunkloader.all_sprites.draw(screen)

    # Main loop for now
    while True:
        # Exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        1

        # Basic movement script

        # Moving camera/player



        # Rendering frame
        #screen.blit(background, (0, 0))


        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()