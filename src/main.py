import pygame
import random
import datetime

import events
from objects.Hammer import Hammer
from objects.Tomb import Tomb
from objects.zombies.NormalZombie import NormalZombie
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
    [NormalZombie(base_pos=(200, 300)), False],
    [NormalZombie(base_pos=(600, 300)), False],
    [NormalZombie(base_pos=(1000, 300)), False],
    [NormalZombie(base_pos=(400, 600)), False],
    [NormalZombie(base_pos=(800, 600)), False],
]
pygame.time.set_timer(events.SPAWN_EVENT, 3000, loops=0)

clock = pygame.time.Clock()
while True:
    current_ms = pygame.time.get_ticks()
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

    ##################################
    # State update stage #

    if pygame.mouse.get_pressed()[0]:
        hammer.smash()
        for zombie in zombies:
            obj, spawned = zombie
            if not spawned:
                continue
            obj_rect = obj.get_rect(SPRITE_MAP)
            if obj_rect.collidepoint(mouse_pos_x, mouse_pos_y):
                zombie[1] = False

    ## Process pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == events.SPAWN_EVENT:
            for zombie in zombies:
                obj, spawned = zombie
                if spawned:
                    continue
                should_spawn = random.random() < 0.3
                zombie[1] = should_spawn
                if should_spawn:
                    obj.spawn()

    ##################################
    # Position update stage #
    ## Hammer as the mouse
    hammer.set_base_pos(mouse_pos_x, mouse_pos_y)

    ##################################
    # Render stage #

    ## Grass lawn background
    screen.blit(SPRITE_MAP[GRASS_IDX], (0, 0))

    ## Tombstone
    for tomb in tombs:
        tomb.draw(screen, SPRITE_MAP)

    ## Zombie
    for zombie in zombies:
        if not zombie[1]:
            continue
        zombie[0].draw(screen, SPRITE_MAP)

    ## Mouse icon
    hammer.draw(screen, SPRITE_MAP)

    ##################################
    # Commit changes #

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
