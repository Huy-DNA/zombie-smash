import pygame

from objects.Tomb import Tomb
from objects.zombies.NormalZombie import NormalZombie
from constants import GRASS_IDX, SCREEN_SIZE, SPRITE_MAP

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

tombs = [
    Tomb(x=100, y=100),
    Tomb(x=500, y=100),
    Tomb(x=900, y=100),
    Tomb(x=300, y=400),
    Tomb(x=700, y=400),
]

while True:
    # State update stage
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    # Render stage
    ## Grass lawn background
    screen.blit(SPRITE_MAP[GRASS_IDX], (0, 0))

    ## Tombstone
    for tomb in tombs:
        tomb.draw_tomb_stone(screen, SPRITE_MAP)

    ## Tomb dirt rock decoration
    for tomb in tombs:
        tomb.draw_tomb_dirt_rocks(screen, SPRITE_MAP)

    # Commit
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
