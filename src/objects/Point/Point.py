from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Point():
    def display_hit_miss(self,hits, misses):
        # render the text
        font = pygame.font.SysFont(None, 50)
        text = f"Hits: {hits} Misses: {misses} "
        text_surface = font.render(text,True,(255,0,0))

        # Blit the text surface to the screen
        text_width = text_surface.get_width()
        x_position = (SCREEN_WIDTH - text_width) // 2
        y_position = 10

        screen.blit(text_surface, (x_position, y_position))