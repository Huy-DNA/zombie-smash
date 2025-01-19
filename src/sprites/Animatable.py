from typing import Optional
import pygame

from sprites.Animation import Animation
from sprites.SpriteMap import SpriteMap


class Animatable:
    """Class for representing an animatable entity such as a zombie"""

    __fps: float
    __start_ms: float
    __animation: Optional[Animation]
    __pos: tuple[float, float]

    def __init__(self):
        self.__fps = 0
        self.__start_ms = 0
        self.__animation = None
        self.__pos = (0, 0)

    def set_animation(self, animation: Animation, start_ms: float):
        self.__animation = animation
        self.__start_ms = start_ms

    def set_fps(self, fps: float):
        self.__fps = fps

    def set_pos(self, x: float, y: float):
        self.__pos = (x, y)

    def is_animation_end(self, current_ms: float) -> bool:
        if not self.__animation:
            return True
        return self.__animation.is_end(self.get_current_frame(current_ms))

    def draw(self, screen: pygame.Surface, current_ms: float, sprites: SpriteMap):
        if not self.__animation:
            return
        sprite = self.__animation.get_sprite(
            self.get_current_frame(current_ms), sprites
        )
        screen.blit(sprite, self.__pos)

    def get_rect(self, current_ms: float, sprites: SpriteMap) -> pygame.Rect:
        if not self.__animation:
            raise Exception("No currently set animation to retrieve Rect")
        return self.__animation.get_sprite(
            self.get_current_frame(current_ms), sprites
        ).get_rect()

    def get_current_frame(self, current_ms: float) -> int:
        delta_ms = current_ms - self.__start_ms
        frame_idx = int(delta_ms * self.__fps / 1000)
        return frame_idx
