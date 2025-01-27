import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Colors and font
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

EASY = 1000
MEDIUM = 800
HARD = 500

MENU_SCENE = "Menu"
EASY_SCENE = "Easy"
MEDIUM_SCENE = "Medium"
HARD_SCENE = "Hard"


def draw_button(text, x, y, width, height, color, hover_color, action=None):
    """Draws a button and executes an action when clicked"""
    """x, y: the top-left corner position of the button"""
    """width, height: the dimesions of the button"""
    mouse = pygame.mouse.get_pos() # get mouse position
    click = pygame.mouse.get_pressed() # handle mouse clicked event

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:            
            action()            
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    # render the button text
    font = pygame.font.SysFont(None, 50)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)



class LevelHandle():
    def __init__(self):
        self.width_button = 200
        self.height_button = 50
        self.font = pygame.font.SysFont(None, 50)
        self.current_level = EASY
        self.current_scene = MENU_SCENE

    def go_to_menu(self):
        """Switch back to the menu"""        
        self.current_scene = MENU_SCENE

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
        
        text_surface = self.font.render(f"{self.current_scene} Level", True, black)
        # text_rect = text_surface.get_rect()
        screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width()) // 2, 100))

        # Back button to return the menu
        draw_button("Back", SCREEN_WIDTH - 200, 10, 100, 50, gray, (150,150,150), self.go_to_menu)