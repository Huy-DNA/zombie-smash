import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import os

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
black = (0,0,0)
# Loading bar dimensions
loading_bar_width = 600
loading_bar_height = 40
loading_bar_x = (SCREEN_WIDTH - loading_bar_width) // 2
loading_bar_y = SCREEN_HEIGHT // 2

def draw_button(text, x, y, width, height, color, hover_color, action=None, set_point=None, set_time=None):
    """Draws a button and executes an action when clicked"""
    """x, y: the top-left corner position of the button"""
    """width, height: the dimesions of the button"""
    mouse = pygame.mouse.get_pos() # get mouse position
    click = pygame.mouse.get_pressed() # handle mouse clicked event

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            display_loading_screen(action(), text)            
            if set_point is not None:
                set_point()

            if set_time is not None:
                set_time()                    
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    # render the button text
    font = pygame.font.SysFont(None, 50)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)



def display_loading_screen(action=None, scene=""):
    """Display a loading screen with a progress bar before entering the given scene"""
    # render background
    screen.fill((255,255,255))    

    # Render Loading text
    font = pygame.font.Font(None, 74)
    loading_text = font.render(f"Loading {scene}", True, (0,0,0))
    text_rect = loading_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(loading_text, text_rect)
    progress = 0    


    while progress <= 100:
        # Draw loading bar background
        pygame.draw.rect(screen, (0,0,0), (loading_bar_x, loading_bar_y, loading_bar_width, loading_bar_height))

        # Draw progress
        filled_width = (progress / 100) * loading_bar_width
        pygame.draw.rect(screen, (0,0,255), (loading_bar_x, loading_bar_y, filled_width, loading_bar_height))

        # Update
        pygame.display.flip()

        pygame.time.delay(20)

        progress += 10

    # Clear the event queue
    pygame.event.clear()

    if action is not None:
        action()

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