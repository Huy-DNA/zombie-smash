import pygame

from sprites.Animation import Direction
from sprites.SpriteMap import SpriteMap


class Static:
    """Class for representing a static entity such as a tomb or background"""

    __sprite_idx: int  # An index into the sprite map
    __base_pos: tuple[float, float]
    __direction: Direction

    def __init__(
        self,
        sprite_idx: int,
        *,
        base_pos: tuple[float, float],
        direction: Direction = Direction.TOP_LEFT,
    ):
        self.__sprite_idx = sprite_idx
        self.__base_pos = base_pos
        self.__direction = direction

    def draw(self, screen: pygame.Surface, sprites: SpriteMap):
        sprite = sprites[self.__sprite_idx]
        rect = sprite.get_rect()
        screen.blit(
            sprite,
            self.__get_topleft_pos(self.__direction, rect.width, rect.height),
        )

    def __get_topleft_pos(
        self, direction: Direction, width: float, height: float
    ) -> tuple[int, int]:
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
