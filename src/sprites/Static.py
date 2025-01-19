import pygame

from sprites.SpriteMap import SpriteMap


class Static:
    """Class for representing a static entity such as a tomb or background"""

    __sprite_idx: int  # An index into the sprite map
    __pos: tuple[float, float]

    def __init__(self, sprite_idx: int, *, x: float, y: float):
        self.__sprite_idx = sprite_idx
        self.__pos = (x, y)

    def draw(self, screen: pygame.Surface, sprites: SpriteMap):
        screen.blit(sprites[self.__sprite_idx], self.__pos)
