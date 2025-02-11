import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.Button.Button import draw_button
from objects.SoundHandler import play_background_music
from constants import BACKGROUND_SOUND_PATH, LOSE_BACKGROUND_SOUND_PATH, VICTORY_BACKGROUND_SOUND_PATH

# Colors and font
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

EASY = 1800
MEDIUM = 1200
HARD = 900

MENU_SCENE = "Menu"
EASY_SCENE = "Easy"
MEDIUM_SCENE = "Medium"
HARD_SCENE = "Hard"
BACK_BUTTON = "Back"

WIN = 'win'
LOSE = 'lose'
CONTINUE = 'continue'
TIME_UP = 'time over'


class LevelHandle:
    def __init__(self):
        self.width_button = 200
        self.height_button = 50        
        self.current_level = EASY
        self.current_scene = MENU_SCENE
        self.game_state = CONTINUE
        self.background_music_path = BACKGROUND_SOUND_PATH
        self.reload_background_music()

    def reload_background_music(self):
        play_background_music(self.background_music_path)

    def go_to_menu(self):
        """Switch back to the menu"""        
        self.set_current_scene(MENU_SCENE)
        self.set_game_state(CONTINUE)
        play_background_music(self.background_music_path)
        
    def go_to_next_level(self):
        if self.get_current_scene() == EASY_SCENE:
            self.set_current_scene(MEDIUM_SCENE)
        elif self.get_current_scene() == MEDIUM_SCENE:
            self.set_current_scene(HARD_SCENE)
        else:
            self.set_current_scene(MENU_SCENE)
        
        self.set_game_state(CONTINUE)        
    
    def play_again(self, prev_scene):
        """Switch back to the previous game"""
        if prev_scene == EASY_SCENE:
            self.set_current_scene(EASY_SCENE)
        elif prev_scene == MEDIUM_SCENE:
            self.set_current_scene(MEDIUM_SCENE)
        else:
            self.set_current_scene(HARD_SCENE)

        self.set_game_state(CONTINUE)

    def easy_level(self):
        """switch to easy scene"""        
        self.current_scene = EASY_SCENE
        if self.game_state != CONTINUE:
            self.set_game_state(CONTINUE)

    def medium_level(self):
        """switch to medium scene"""
        self.current_scene = MEDIUM_SCENE
        if self.game_state != CONTINUE:
            self.set_game_state(CONTINUE)        

    def hard_level(self):
        """switch to hard scene"""        
        self.current_scene = HARD_SCENE       
        if self.game_state != CONTINUE:
            self.set_game_state(CONTINUE) 

    def draw_menu(self):
        """Draws the main menu with buttons."""
        # Title
        # title_surface = font.render("Select Difficulty Level", True, black)
        # title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
        # screen.blit(title_surface, title_rect)

        # Draw gameplay buttons
        draw_button("Easy", (SCREEN_WIDTH - self.width_button) // 2, 360, self.width_button, self.height_button, green, (0, 200, 0), self.easy_level)
        draw_button("Medium", (SCREEN_WIDTH - self.width_button) // 2, 440, self.width_button, self.height_button, blue, (0, 0, 200), self.medium_level)
        draw_button("Hard", (SCREEN_WIDTH - self.width_button) // 2, 520, self.width_button, self.height_button, red, (200, 0, 0), self.hard_level)

    def draw_game_scene(self,level):
        """Draw the selected game scene"""        
        if level == "Easy":
            self.current_level = EASY
        elif level == "Medium":
            self.current_level = MEDIUM
        else:   
            self.current_level = HARD

        font = pygame.font.SysFont(None, 50)
        
        text_surface = font.render(f"{self.current_scene} Level", True, black)
        # text_rect = text_surface.get_rect()
        # screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width()) // 2, 50))
        screen.blit(text_surface, (10, 10))

        # Back button to return the menu
        draw_button(BACK_BUTTON, SCREEN_WIDTH - 200, 10, 100, 50, gray, (150,150,150), self.go_to_menu)        

    def get_current_scene(self):
        return self.current_scene
    
    def get_current_level(self):
        return self.current_level
    
    def set_current_scene(self, scene):
        self.current_scene = scene    
        
    def set_game_state(self, state):
        self.game_state = state
        if self.game_state == TIME_UP or self.game_state == LOSE:
            self.background_music_path = LOSE_BACKGROUND_SOUND_PATH
        elif self.game_state == WIN:
            self.background_music_path = VICTORY_BACKGROUND_SOUND_PATH
        else:
            self.background_music_path = BACKGROUND_SOUND_PATH
        self.reload_background_music()

    def get_game_state(self):
        return self.game_state