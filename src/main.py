import pygame

from objects.Hammer import Hammer
from objects.Tomb import Tomb
from objects.zombies.NormalZombie import NormalZombie
from constants import GRASS_IDX, ICON_PATH, SCREEN_SIZE, SPRITE_MAP

pygame.init()

pygame.display.set_caption("Zombie smash")
pygame.display.set_icon(pygame.image.load(ICON_PATH))
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCREEN_SIZE)

tombs = [
    Tomb(x=100, y=100),
    Tomb(x=500, y=100),
    Tomb(x=900, y=100),
    Tomb(x=300, y=400),
    Tomb(x=700, y=400),
]
hammer = Hammer()

clock = pygame.time.Clock()
while True:
    current_ms = pygame.time.get_ticks()
    hammer_rect = hammer.get_rect(current_ms, SPRITE_MAP)

    ##################################
    # State update stage #

    ## Hammer as the mouse
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    hammer.set_pos(
        mouse_pos_x - hammer_rect.width / 2, mouse_pos_y - hammer_rect.height / 2
    )

    if pygame.mouse.get_pressed()[0]:
        hammer.smash(current_ms)

    ## Process pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    ##################################
    # Render stage #

    ## Grass lawn background
    screen.blit(SPRITE_MAP[GRASS_IDX], (0, 0))

    ## Tombstone
    for tomb in tombs:
        tomb.draw_tomb_stone(screen, SPRITE_MAP)

    ## Tomb dirt rock decoration
    for tomb in tombs:
        tomb.draw_tomb_dirt_rocks(screen, SPRITE_MAP)

    ## Mouse icon
    hammer.draw(screen, current_ms, SPRITE_MAP)

    ##################################
    # Commit changes #

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
