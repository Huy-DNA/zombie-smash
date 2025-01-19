from typing import Optional
import pygame

from sprites.Animation import Animation
from sprites.SpriteMap import SpriteMap

class Animatable():
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
        delta_ms = current_ms - self.__start_ms
        frame_idx = int(delta_ms * self.__fps / 1000)
        return self.__animation.is_end(frame_idx)

    def draw(self, screen: pygame.Surface, current_ms: float, sprites: SpriteMap):
        if not self.__animation:
            return
        delta_ms = current_ms - self.__start_ms
        frame_idx = int(delta_ms * self.__fps / 1000)
        sprite = self.__animation.get_sprite(frame_idx, sprites)
        screen.blit(sprite, self.__pos)
