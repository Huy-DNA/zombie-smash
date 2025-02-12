from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.Level.Level import LevelHandle, LOSE, TIME_UP
from objects.Time.Time import Time
from objects.Button.Button import draw_button
import os
from objects.SoundHandler import play_background_music
import pygame
from constants import LOSE_BACKGROUND_SOUND_PATH, VICTORY_BACKGROUND_SOUND_PATH

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


BLACK = (0, 0, 0)
TRANSPARENT_BLACK = (0, 0, 0, 128)  # Semi-transparent overlay
BORDER_COLOR = (239, 176, 54)  # white
WHITE = (255, 255, 255)
VICTORY_COLOR = (255, 217, 95)
LOSE_COLOR = (229, 32, 32)


def draw_blur_background():
    """Draw a semi-transparent gray overlay for a blur effect."""
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(180)  # Transparency level (0 to 255)
    overlay.fill((200, 200, 200))  # Light gray
    screen.blit(overlay, (0, 0))


class Point:
    def __init__(self, hits, misses):
        self.hits = hits
        self.misses = misses

    def display_hit_miss(
        self, hits, misses, y_position=0, colors=(255, 0, 0), font_size=50
    ):
        # render the text
        font = pygame.font.SysFont(None, font_size)

        # Set hits and misses
        self.set_hits(hits)
        self.set_misses(misses)

        # Render messagge
        text = f"Hits: {hits} Misses: {misses} "
        text_surface = font.render(text, True, colors)

        # Blit the text surface to the screen
        text_width = text_surface.get_width()
        x_position = (SCREEN_WIDTH - text_width) // 2

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

    def draw_scenes(self, levelObject: LevelHandle, timeObject: Time):
        font = pygame.font.Font(None, 36)
        # create dark transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill(TRANSPARENT_BLACK)
        screen.blit(overlay, (0, 0))

        # rectangle dimensions
        rect_width, rect_height = 500, 200
        rect_x = (SCREEN_WIDTH - rect_width) // 2
        rect_y = (SCREEN_HEIGHT - rect_height) // 2

        # draw border
        border_thickness = 5
        pygame.draw.rect(
            screen,
            BORDER_COLOR,
            (
                rect_x - border_thickness,
                rect_y - border_thickness,
                rect_width + 2 * border_thickness,
                rect_height + 2 * border_thickness,
            ),
            0,
            10,
        )

        # draw inner
        pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))
        # render text
        time_res = ""
        if levelObject.get_game_state() == TIME_UP:
            time_res = "Time's up"
        else:
            if timeObject.get_minutes() < 1:
                time_res = f"{timeObject.get_seconds()}s"
            else:
                time_res = f"{timeObject.get_minutes()}:{timeObject.get_seconds()}"

        level_text = font.render(
            f"{'Level:': <11}{levelObject.get_current_scene():^70}", True, BLACK
        )
        hits_text = font.render(f"{'Hits:': <11}{self.get_hits():^70}", True, BLACK)
        misses_text = font.render(
            f"{'Misses:': <10}{self.get_misses():^65}", True, BLACK
        )

        # Time render
        time = f"{'Time left:':<10}{time_res:^69}"
        time_text = font.render(time, True, BLACK)

        # Position text
        screen.blit(level_text, (rect_x + 20, rect_y + 40))
        screen.blit(hits_text, (rect_x + 20, rect_y + 80))
        screen.blit(misses_text, (rect_x + 20, rect_y + 120))
        screen.blit(time_text, (rect_x + 20, rect_y + 160))

    def draw_ending_scene(self, levelObject: LevelHandle, timeObject: Time):
        # render lose win text
        font_state = pygame.font.Font(None, 100)
        win_text = font_state.render("Victory", True, VICTORY_COLOR)
        lose_text = font_state.render("Lose", True, LOSE_COLOR)

        self.draw_scenes(levelObject, timeObject)
        # draw button when win or lose
        draw_button(
            "Return",
            (SCREEN_WIDTH - 400) // 2,
            SCREEN_HEIGHT // 2 + 200,
            200,
            50,
            (255, 255, 255),
            (0, 200, 0),
            levelObject.go_to_menu,
            set_point=self.set_points,
            set_time=timeObject.set_time(90),
        )
        if (
            levelObject.get_game_state() == LOSE
            or levelObject.get_game_state() == TIME_UP
        ):
            # Display lose text
            screen.blit(lose_text, ((SCREEN_WIDTH - 200) // 2, 50))
            # Draw button play again
            draw_button(
                "Play again",
                (SCREEN_WIDTH + 50) // 2,
                SCREEN_HEIGHT // 2 + 200,
                200,
                50,
                (255, 255, 255),
                (0, 200, 0),
                lambda: (levelObject.play_again(levelObject.get_current_scene())),
                set_point=self.set_points,
                set_time=timeObject.set_time(90),
            )
        else:
            # Display win text
            screen.blit(win_text, ((SCREEN_WIDTH - 200) // 2, 50))
            # draw button continue
            draw_button(
                "Continue",
                (SCREEN_WIDTH + 50) // 2,
                SCREEN_HEIGHT // 2 + 200,
                200,
                50,
                (255, 255, 255),
                (0, 200, 0),
                lambda: levelObject.go_to_next_level,
                set_point=self.set_points,
                set_time=timeObject.set_time(90),
            )

        # Update the display
        pygame.mouse.set_visible(True)
        pygame.display.flip()

