import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Playload_adventure_game")
clock = pygame.time.Clock()

cameraX = 0
cameraY = 0

background = pygame.Surface((800,400))
colorBlock = pygame.Surface((100,50))
colorBlockr = colorBlock.get_rect(center = (400,225))
player = pygame.Surface((40,50))
player_rect = player.get_rect(center = (400, 200))

#Main loop for now
while True:
    #Exit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    1
    
    
    #Basic movement script
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and keys[pygame.K_s]:
        cameraY = 0
    elif keys[pygame.K_w]:
        cameraY = 10
    elif keys[pygame.K_s]:
        cameraY = -10
    else:
        cameraY = 0
    if keys[pygame.K_a] and keys[pygame.K_d]:
        cameraX = 0
    elif keys[pygame.K_a]:
        cameraX = 10
    elif keys[pygame.K_d]:
        cameraX = -10
    else:
        cameraX = 0
    1


    #Moving camera/player
    colorBlockr.y += cameraY
    colorBlockr.x += cameraX



    #Rendering frame
    screen.blit(background, (0,0))
    pygame.draw.rect(screen,"Red",colorBlockr)
    pygame.draw.rect(screen,"Blue",player_rect)

    pygame.display.update()
    clock.tick(60)