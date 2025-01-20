import pygame
import random
import datetime

import events
from objects.Hammer import Hammer
from objects.Tomb import Tomb
from objects.zombies.NormalZombie import NormalZombie, ZombieAnimation
from constants import GRASS_IDX, ICON_PATH, SCREEN_SIZE, SPRITE_MAP

pygame.init()
random.seed(datetime.datetime.now().ctime())

pygame.display.set_caption("Zombie smash")
pygame.display.set_icon(pygame.image.load(ICON_PATH))
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCREEN_SIZE)

hammer = Hammer()
tombs = [
    Tomb(x=100, y=100),
    Tomb(x=500, y=100),
    Tomb(x=900, y=100),
    Tomb(x=300, y=400),
    Tomb(x=700, y=400),
]
zombies = [
    # [Zombie instance, is spawned]
    [NormalZombie(), False],
    [NormalZombie(), False],
    [NormalZombie(), False],
    [NormalZombie(), False],
    [NormalZombie(), False],
]
pygame.time.set_timer(events.SPAWN_EVENT, 3000, loops = 0)

clock = pygame.time.Clock()
while True:
    current_ms = pygame.time.get_ticks()
    hammer_rect = hammer.get_rect(current_ms, SPRITE_MAP)

    ##################################
    # State update stage #

    if pygame.mouse.get_pressed()[0]:
        hammer.smash(current_ms)

    ## Process pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == events.SPAWN_EVENT:
            for zombie in zombies:
                obj, spawned = zombie
                if spawned: continue
                should_spawn = random.random() < 0.3
                zombie[1] = should_spawn
                if should_spawn:
                    obj.spawn(current_ms)

    ##################################
    # Position update stage #
    ## Zombie
    for i, zombie in enumerate(zombies):
        if not zombie[1]:
            continue
        tomb_pos = tombs[i].get_pos()
        zombie_rect = zombie[0].get_rect(current_ms, SPRITE_MAP)
        zombie[0].set_pos(
            tomb_pos[0] + 100 - zombie_rect.width / 2, tomb_pos[1] + 190 - zombie_rect.height
        )

    ## Hammer as the mouse
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    hammer.set_pos(
        mouse_pos_x - hammer_rect.width / 2, mouse_pos_y - hammer_rect.height / 2
    )

    ##################################
    # Render stage #

    ## Grass lawn background
    screen.blit(SPRITE_MAP[GRASS_IDX], (0, 0))

    ## Tombstone
    for tomb in tombs:
        tomb.draw_tomb_stone(screen, SPRITE_MAP)

    for zombie in zombies:
        if not zombie[1]:
            continue
        zombie[0].draw(screen, current_ms, SPRITE_MAP)

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
