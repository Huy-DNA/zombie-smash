import pygame
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

COUNTDOWN_TIME = 120
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Time():
    def __init__(self, total_time):
        self.countdown_time = COUNTDOWN_TIME
        self.start_time = time.time()
        self.start_ticks = pygame.time.get_ticks() # Record the time started
        self.total_time = total_time # Set the total time to countdown
        self.minutes = 0
        self.seconds = 0

    def display_countdown_time(self):        
        font = pygame.font.Font(None, 74)
        elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000
        remaining_time = max(0, self.total_time - int(elapsed_time))

        # Convert time to minutes:seconds format
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_text = f"{int(minutes):02}:{int(seconds):02}"

        # set minutes and seconds left
        self.set_minutes(minutes)
        self.set_seconds(seconds)

        # render the timer
        text_surface = font.render(timer_text, True, (255,0,0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)

        return remaining_time == 0
        
    def reduce_time_by_ms(self,ms):
        self.start_time += ms

    def set_time(self, time):
        self.total_time = time
        self.start_ticks = pygame.time.get_ticks()

    def get_time(self):
        return self.total_time
    
    def get_minutes(self):
        return self.minutes
    
    def set_minutes(self, minutes):
        self.minutes = minutes
    
    def get_seconds(self):
        return self.seconds
    
    def set_seconds(self, seconds):
        self.seconds = seconds
            

