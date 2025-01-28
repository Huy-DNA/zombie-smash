from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.Level.Level import LevelHandle
from objects.Button.Button import draw_button

import pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_blur_background():
    """Draw a semi-transparent gray overlay for a blur effect."""
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(180)  # Transparency level (0 to 255)
    overlay.fill((200, 200, 200))  # Light gray
    screen.blit(overlay, (0, 0))

class Point():
    def __init__(self, hits, misses):
        self.hits = hits
        self.misses = misses
        self.game_over = False

    def display_hit_miss(self,hits, misses):
        # render the text
        font = pygame.font.SysFont(None, 50)

        # Set hits and misses
        self.set_hits(hits)
        self.set_misses(misses)

        # Render messagge
        text = f"Hits: {hits} Misses: {misses} "
        text_surface = font.render(text,True,(255,0,0))

        # Blit the text surface to the screen
        text_width = text_surface.get_width()
        x_position = (SCREEN_WIDTH - text_width) // 2
        y_position = 10

        screen.blit(text_surface, (x_position, y_position))

    def get_hits(self):
        return self.hits
    
    def set_hits(self, hits):
        self.hits = hits
    
    def get_misses(self):
        return self.misses
    
    def set_misses(self, misses):
        self.misses = misses

    def draw_ending_scene(self, text, levelObject: LevelHandle):
        # fill the screen with shadow background
        draw_blur_background()

        # Initialize font
        font = pygame.font.SysFont(None, 74)
        # Render Victory text
        text = font.render(f"{text}", True, (255, 232, 147))
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(text, rect)

        print(levelObject.get_current_scene())
        draw_button("Return", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 , 200, 50, (255,255,255), (0, 200, 0), levelObject.go_to_menu)
        draw_button("Play again", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, 200, 50, (255,255,255), (0, 200, 0), levelObject.go_to_menu)

        # Update the display
        pygame.display.flip()

    def get_game_over(self):
        return self.game_over
    
    def set_game_over(self, current_game_state):
        self.game_over = current_game_state