import pygame
import random
import datetime

import events
from objects.Hammer import Hammer
from objects.SpawningSpot import SpawningSpot
from constants import GRASS_IDX, ICON_PATH, SCREEN_SIZE, SPRITE_MAP

pygame.init()
random.seed(datetime.datetime.now().ctime())

pygame.display.set_caption("Zombie smash")
pygame.display.set_icon(pygame.image.load(ICON_PATH))
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCREEN_SIZE)

hammer = Hammer()
spawning_spots = [
    SpawningSpot(base_pos=(100,100)),
    SpawningSpot(base_pos=(500,100)),
    SpawningSpot(base_pos=(900,100)),
    SpawningSpot(base_pos=(300,400)),
    SpawningSpot(base_pos=(700,400)),
]
pygame.time.set_timer(events.SPAWN_EVENT, 3000, loops=0)

hits = 0
misses = 0
clock = pygame.time.Clock()
last_mouse_state = pygame.mouse.get_pressed()
while True:
    current_ms = pygame.time.get_ticks()
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

    ##################################
    # State update stage #

    current_mouse_state = pygame.mouse.get_pressed()
    if not last_mouse_state[0] and current_mouse_state[0]:
        hammer.smash()
        for spot in spawning_spots:
            active_zombie = spot.get_active_zombie()
            if active_zombie is not None and active_zombie.get_rect(SPRITE_MAP).collidepoint(mouse_pos_x, mouse_pos_y):
                spot.kill_zombie()
                hits += 1
                break
        else:
            misses += 1
    last_mouse_state = current_mouse_state

    ## Process pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == events.SPAWN_EVENT:
            for spot in spawning_spots:
                if not spot.has_zombie() and random.random() < 0.3:
                    spot.spawn_zombie()

    ## Try despawning zombies
    for spot in spawning_spots:
        if spot.get_spawned_time() > 3000:
            spot.despawn_zombie()

    ##################################
    # Position update stage #
    ## Hammer as the mouse
    hammer.set_base_pos(mouse_pos_x, mouse_pos_y)

    ##################################
    # Render stage #

    ## Grass lawn background
    screen.blit(SPRITE_MAP[GRASS_IDX], (0, 0))

    ## Spawning spots
    for spot in spawning_spots:
        spot.draw(screen, SPRITE_MAP)

    ## Mouse icon
    hammer.draw(screen, SPRITE_MAP)

    ##################################
    # Commit changes #

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
