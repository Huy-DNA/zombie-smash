import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.Button.Button import draw_button

# Colors and font
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

EASY = 1500
MEDIUM = 1000
HARD = 500

MENU_SCENE = "Menu"
EASY_SCENE = "Easy"
MEDIUM_SCENE = "Medium"
HARD_SCENE = "Hard"

WIN = 'win'
LOSE = 'lose'
CONTINUE = 'continue'


class LevelHandle:
    def __init__(self):
        self.width_button = 200
        self.height_button = 50        
        self.current_level = EASY
        self.current_scene = MENU_SCENE
        self.gameover = False
        self.game_state = CONTINUE

    def go_to_menu(self):
        """Switch back to the menu"""        
        self.current_scene = MENU_SCENE
        self.game_state = CONTINUE
    
    def play_again(self, prev_scene):
        """Switch back to the previous game"""
        if prev_scene == EASY_SCENE:
            self.current_scene = EASY_SCENE
        elif prev_scene == MEDIUM_SCENE:
            self.current_scene = MEDIUM_SCENE
        else:
            self.current_scene = HARD_SCENE

        self.game_state = CONTINUE

    def easy_level(self):
        """switch to easy scene"""        
        self.current_scene = EASY_SCENE        

    def medium_level(self):
        """switch to medium scene"""
        self.current_scene = MEDIUM_SCENE        

    def hard_level(self):
        """switch to hard scene"""        
        self.current_scene = HARD_SCENE        

    def draw_menu(self):
        """Draws the main menu with buttons."""
        # Title
        # title_surface = font.render("Select Difficulty Level", True, black)
        # title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
        # screen.blit(title_surface, title_rect)

        # Draw buttons
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
        draw_button("Back", SCREEN_WIDTH - 200, 10, 100, 50, gray, (150,150,150), self.go_to_menu)        

    def get_current_scene(self):
        return self.current_scene
    
    def get_current_level(self):
        return self.current_level
    
    def set_current_scene(self, scene):
        self.current_scene = scene

    def get_gameover(self):
        return self.gameover
        
    def set_game_state(self, state):
        self.game_state = state

    def get_game_state(self):
        return self.game_state