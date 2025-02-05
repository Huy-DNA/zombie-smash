import pygame
import random
import datetime
import time

import events
from objects.Hammer import Hammer
from objects.SpawningSpot import SpawningSpot
from objects.Level.Level import LevelHandle, WIN, LOSE, TIME_UP, EASY_SCENE, MEDIUM_SCENE, HARD_SCENE, MENU_SCENE
from objects.Point.Point import Point
from objects.Time.Time import Time
from constants import GRASS_IDX, ICON_PATH, SCREEN_SIZE, SPRITE_MAP, SCREEN_WIDTH, SCREEN_HEIGHT

import os

pygame.init()
random.seed(datetime.datetime.now().ctime())

pygame.display.set_caption("Zombie smash")
pygame.display.set_icon(pygame.image.load(ICON_PATH))
# pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCREEN_SIZE)

hammer = Hammer()
spawning_spots = [
    SpawningSpot(base_pos=(100,100)),
    SpawningSpot(base_pos=(500,100)),
    SpawningSpot(base_pos=(900,100)),
    SpawningSpot(base_pos=(300,400)),
    SpawningSpot(base_pos=(700,400)),
]


# load the background
try:
    background_image = pygame.image.load(f"{os.getcwd()}/assets/background/smashing-zombie-game.webp")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error as e:
    print('Cannot load the image', e)
    pygame.quit()
    exit()

# load win, lose bg
try:
    win_image = pygame.image.load(f"{os.getcwd()}/assets/background/victory-scene.webp")
    win_image = pygame.transform.scale(win_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    loss_image = pygame.image.load(f"{os.getcwd()}/assets/background/loss.webp")
    loss_image = pygame.transform.scale(loss_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error as e:
    print('Cannot load the image', e)
    pygame.quit()
    exit()


# current scene and game states
# hits = 0
# misses = 0

# check game condition
def check_game_condition():
    win = 5
    easy_lose = 3
    med_lose = 2
    hard_lose = 1

    if point_object.get_hits() == win:
        level_object.set_game_state(WIN)
        return
        
    if level_object.get_current_scene() == EASY_SCENE:
        if point_object.get_misses() == easy_lose:
            level_object.set_game_state(LOSE)
    elif level_object.get_current_scene() == MEDIUM_SCENE:
        if point_object.get_misses() == med_lose:
            level_object.set_game_state(LOSE)
    else:
        if point_object.get_misses() == hard_lose:
            level_object.set_game_state(LOSE)

level_object = LevelHandle()
point_object = Point(0, 0)
time_object = Time(93)
start = False

pygame.time.set_timer(events.SPAWN_EVENT, level_object.get_current_level(), loops=0)

clock = pygame.time.Clock()
last_mouse_state = pygame.mouse.get_pressed()
running = True


while running:         
    current_ms = pygame.time.get_ticks()
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    
    ## Process pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == events.SPAWN_EVENT:
            for spot in spawning_spots:
                if not spot.has_zombie() and random.random() < 0.3:
                    spot.spawn_zombie()

    # check game over condition
    if level_object.get_game_state() == LOSE or level_object.get_game_state() == TIME_UP and level_object.get_current_scene() != MENU_SCENE:
        screen.blit(loss_image, (0,0))
        point_object.draw_ending_scene(level_object, time_object)          
        continue
    elif level_object.get_game_state() == WIN and level_object.get_current_scene() != MENU_SCENE:
        screen.blit(win_image, (0,0))
        point_object.draw_ending_scene(level_object, time_object)        
        continue     

    ##################################
    # State update stage #    
    
    
    current_mouse_state = pygame.mouse.get_pressed()
    if last_mouse_state[0] == 0 and current_mouse_state[0] == 1:
        if start:
            hammer.smash()
            for spot in spawning_spots:
                active_zombie = spot.get_active_zombie()
                if active_zombie is not None and active_zombie.get_rect(SPRITE_MAP).collidepoint(mouse_pos_x, mouse_pos_y):
                    spot.kill_zombie()
                    #hits += 1
                    point_object.set_hits(point_object.get_hits() + 1)
                    break
            else:
                # misses += 1                
                point_object.set_misses(point_object.get_misses() + 1)
        else:            
            time_object.set_time(92)
    last_mouse_state = current_mouse_state

    
    ## Try despawning zombies
    for spot in spawning_spots:
        if spot.get_spawned_time() >= level_object.get_current_level():
            spot.despawn_zombie()
        # if not spot.has_zombie() and spot.can_spawn(level_object.get_current_level()):
        #     spot.despawn_zombie()

    ##################################
    # Position update stage #
    ## Hammer as the mouse
    hammer.set_base_pos(mouse_pos_x, mouse_pos_y)

    ##################################
    # Render stage #

    if level_object.get_current_scene() == "Menu":
        screen.blit(background_image, (0,0))
        pygame.mouse.set_visible(True)
        # reset the hits, misses point               
    else:                
        ## Grass lawn background
        screen.blit(SPRITE_MAP[GRASS_IDX], (0, 0))

        ## Spawning spots
        for spot in spawning_spots:
            spot.draw(screen, SPRITE_MAP)

        ## Mouse icon
        hammer.draw(screen, SPRITE_MAP)           

        # Display the point                       
        point_object.display_hit_miss(point_object.get_hits(), point_object.get_misses(), 10)
        # Render timer        
        time_up = time_object.display_countdown_time()
        if time_up:
            level_object.set_game_state(TIME_UP) 

        pygame.mouse.set_visible(False)
        

    ##################################
    # Commit changes #
    # scene render
    if level_object.get_current_scene() == MENU_SCENE:
        level_object.draw_menu()
        start = False
        point_object.set_points()
    elif level_object.get_current_scene() == EASY_SCENE:    
        # display_loading_screen()        
        level_object.draw_game_scene(EASY_SCENE)        
        # check win lose condition
        check_game_condition()
        start = True
    elif level_object.get_current_scene() == MEDIUM_SCENE:
        level_object.draw_game_scene(MEDIUM_SCENE)
        # check win lose condition
        check_game_condition()
        start = True
    else:
        level_object.draw_game_scene(HARD_SCENE)
        # check win lose condition
        check_game_condition()
        start = True
    pygame.display.flip()


    clock.tick(60)

pygame.quit()
