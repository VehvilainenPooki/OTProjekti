import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Playload_adventure_game")
clock = pygame.time.Clock()

colorBlock = pygame.Surface((100,200))
colorBlock.fill("Red")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(colorBlock,(0,0))

    pygame.display.update()
    clock.tick(60)