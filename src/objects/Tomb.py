import pygame

from constants import TOMB_IDX, TOMB_ROCKS_IDX
from sprites.SpriteMap import SpriteMap
from sprites.Static import Static


class Tomb:
    __tomb_stone: Static
    __tomb_dirt_rocks: list[Static]
    __base_pos: tuple[float, float]

    def __init__(self, *, base_pos: tuple[float, float]):
        self.__base_pos = base_pos
        self.__tomb_stone = Static(TOMB_IDX, base_pos=base_pos)
        self.__tomb_dirt_rocks = [
            Static(TOMB_ROCKS_IDX, base_pos=(base_pos[0] - 30, base_pos[1] + 170)),
            Static(TOMB_ROCKS_IDX, base_pos=(base_pos[0] + 40, base_pos[1] + 160)),
        ]

    def get_base_pos(self) -> tuple[float, float]:
        return self.__base_pos

    def draw(self, screen: pygame.Surface, sprites: SpriteMap):
        self.__tomb_stone.draw(screen, sprites)
        for sprite in self.__tomb_dirt_rocks:
            sprite.draw(screen, sprites)
            sprite.draw(screen, sprites)
