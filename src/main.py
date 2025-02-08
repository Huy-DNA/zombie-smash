import pygame
import random
import datetime

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
    med_lose = 3
    hard_lose = 2

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
# def draw quit button
def quit_button(button_pos_dim, optional_text=None, action=None):
    mouse = pygame.mouse.get_pos() # get mouse position
    click = pygame.mouse.get_pressed() # handle mouse clicked event
    logout_icon = pygame.image.load(f"{os.getcwd()}/assets/turn-off.png")
    logout_icon = pygame.transform.scale(logout_icon, (30, 30))
    # button_pos_dim: x, y, width, height
    x,y,width,height = button_pos_dim
    
    # handle mouse click
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, (238,238,238), button_pos_dim)
        if click[0] and action is not None:
            action()
    else:
        pygame.draw.rect(screen, (180,180,180), button_pos_dim)

    if optional_text is None:
        # icon x, y position
        icon_x = x + (width - logout_icon.get_width()) // 2
        icon_y = y + (height - logout_icon.get_height()) // 2
        screen.blit(logout_icon, (icon_x, icon_y))
    else:
        font = pygame.font.Font(None, 30)
        text_surface = font.render(optional_text, True, (0,0,0))
        text_x = x + (width - text_surface.get_width()) // 2
        text_y = y + (height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))



def display_quit_screen():
    font = pygame.font.Font(None, 50) # create font size
    # color
    TRANSPARENT_BLACK = (0, 0, 0, 128)  # Semi-transparent overlay
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    # create dark transparent overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill(TRANSPARENT_BLACK)
    screen.blit(overlay, (0,0))
    # rect width height
    rect_w, rect_h = 500, 200
    rect_x, rect_y = (SCREEN_WIDTH - rect_w) // 2, (SCREEN_HEIGHT - rect_h) // 2
    # draw rect
    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_w, rect_h))
    # draw quit text
    text_surface = font.render("DO YOU WANT TO QUIT?", True, BLACK)
    text_x = rect_x + (rect_w - text_surface.get_width()) // 2
    text_y = rect_y + (rect_h - text_surface.get_height()) // 2
    screen.blit(text_surface, (text_x, text_y))

    # draw yes, no button
    yes_pos_dim = (rect_x - 100 + (rect_w - 100) // 2, rect_y + (rect_h - 40), 100, 30)
    no_pos_dim = (rect_x + 100 + (rect_w - 100) // 2, rect_y + (rect_h - 40), 100, 30)
    quit_button(yes_pos_dim, optional_text="YES", action=lambda: set_running(False))
    quit_button(no_pos_dim,optional_text="NO", action=lambda: set_quit_screen(False))

def set_quit_screen(val):
    global quit_screen
    quit_screen = val

def set_running(val):
    global running
    running = val

level_object = LevelHandle()
point_object = Point(0, 0)
time_object = Time(90)
start = False
quit_screen = False

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
    if (level_object.get_game_state() == LOSE or level_object.get_game_state() == TIME_UP) and level_object.get_current_scene() != MENU_SCENE:
        # screen.blit(loss_image, (0,0))
        screen.blit(SPRITE_MAP[GRASS_IDX], (0, 0))        
        
        point_object.draw_ending_scene(level_object, time_object)          
        continue
    elif level_object.get_game_state() == WIN and level_object.get_current_scene() != MENU_SCENE:
        # screen.blit(win_image, (0,0))
        screen.blit(SPRITE_MAP[GRASS_IDX], (0, 0))
        
        point_object.draw_ending_scene(level_object, time_object)        
        continue  

    ##################################
    # State update stage #    
    if quit_screen:
        screen.blit(background_image, (0,0))        
        display_quit_screen()
        pygame.display.flip()
        continue
    
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
            time_object.set_time(90)
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
        # Draw quit button
        button_pos_dim = (SCREEN_WIDTH - 100, 10, 50, 50)
        quit_button(button_pos_dim,action=lambda: set_quit_screen(True))
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
