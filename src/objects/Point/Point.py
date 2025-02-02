from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.Level.Level import LevelHandle, WIN, LOSE
from objects.Time.Time import Time
from objects.Button.Button import draw_button
import os

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

    def set_points(self):
        self.hits = 0
        self.misses = 0

    def draw_ending_scene(self,levelObject: LevelHandle, timeObject: Time):
        # Initialize font                
        
        # draw button when win or lose
        draw_button("Return", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 , 200, 50, (255,255,255), (0, 200, 0), levelObject.go_to_menu, set_point=self.set_points)
        if levelObject.get_game_state() == LOSE:
            draw_button("Play again", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, 200, 50, (255,255,255), (0, 200, 0), 
                        lambda: (levelObject.play_again(levelObject.get_current_scene())), set_point=self.set_points, set_time=timeObject.set_time(93))
        else:
            draw_button("Continue", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, 200, 50, (255,255,255), (0, 200, 0), lambda: levelObject.go_to_menu, set_point=self.set_points, set_time=timeObject.set_time(93))
                    

        # Update the display
        pygame.mouse.set_visible(True)        
        pygame.display.flip()    