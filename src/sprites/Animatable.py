from typing import Optional
import pygame

from sprites.Animation import Direction
from sprites.AnimationSet import AnimationSet
from sprites.SpriteMap import SpriteMap


class Animatable:
    """Class for representing an animatable entity such as a zombie"""

    __animation_set: Optional[AnimationSet]
    __base_pos: tuple[float, float]
    __start_ms: float

    def __init__(self, *, base_pos: tuple[float, float] = (0, 0), start_ms: float = 0):
        self.__base_pos = base_pos
        self.__animation_set = None
        self.__start_ms = start_ms or pygame.time.get_ticks()

    def set_animation_set(self, animation_set: AnimationSet, *, start_ms: float = 0):
        self.__animation_set = animation_set
        self.__start_ms = start_ms or pygame.time.get_ticks()

    def set_base_pos(self, x: float, y: float):
        self.__base_pos = (x, y)

    def get_base_pos(self) -> tuple[float, float]:
        return self.__base_pos

    def draw(self, screen: pygame.Surface, sprites: SpriteMap):
        if not self.__animation_set:
            return
        sprite, direction = self.__animation_set.get_sprite(
            self.get_current_frame(), sprites
        )
        sprite_rect = sprite.get_rect()
        screen.blit(sprite, self.__get_topleft_pos(direction, sprite_rect.width, sprite_rect.height))

    def get_rect(self, sprites: SpriteMap) -> pygame.Rect:
        if not self.__animation_set:
            raise Exception("No current rect")
        sprite, direction = self.__animation_set.get_sprite(
            self.get_current_frame(), sprites
        )
        rect = sprite.get_rect()
        rect.topleft = self.__get_topleft_pos(direction, rect.width, rect.height)
        return rect

    def get_current_frame(self) -> int:
        if not self.__animation_set:
            raise Exception("No current frame")
        delta_ms = pygame.time.get_ticks() - self.__start_ms
        frame_idx = int(delta_ms * self.__animation_set.fps / 1000)
        return frame_idx

    def __get_topleft_pos(self, direction: Direction, width: float, height: float) -> tuple[int, int]:
        match direction:
            case Direction.TOP_LEFT:
                pos = self.__base_pos
            case Direction.TOP_CENTER:
                pos = (self.__base_pos[0] - width / 2, self.__base_pos[1])
            case Direction.TOP_RIGHT:
                pos = (self.__base_pos[0] - width, self.__base_pos[1])
            case Direction.CENTER_LEFT:
                pos = (self.__base_pos[0], self.__base_pos[1] - height / 2)
            case Direction.CENTER_CENTER:
                pos = (self.__base_pos[0] - width / 2, self.__base_pos[1] - height / 2)
            case Direction.CENTER_RIGHT:
                pos = (self.__base_pos[0] - width, self.__base_pos[1] - height / 2)
            case Direction.BOTTOM_LEFT:
                pos = (self.__base_pos[0], self.__base_pos[1] - height)
            case Direction.BOTTOM_CENTER:
                pos = (self.__base_pos[0] - width / 2, self.__base_pos[1] - height)
            case Direction.BOTTOM_RIGHT:
                pos = (self.__base_pos[0] - width, self.__base_pos[1] - height)
        return (int(pos[0]), int(pos[1]))
