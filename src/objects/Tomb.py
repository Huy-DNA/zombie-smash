import pygame

from constants import TOMB_IDX, TOMB_ROCKS_IDX
from sprites.SpriteMap import SpriteMap
from sprites.Static import Static


class Tomb:
    __tomb_stone: Static
    __tomb_dirt_rocks: list[Static]

    def __init__(self, *, x: float, y: float):
        self.__tomb_stone = Static(TOMB_IDX, x=x, y=y)
        self.__tomb_dirt_rocks = [
            Static(TOMB_ROCKS_IDX, x=x - 30, y=y + 170),
            Static(TOMB_ROCKS_IDX, x=x + 40, y=y + 160)
        ]

    def draw_tomb_stone(self, screen: pygame.Surface, sprites: SpriteMap):
        self.__tomb_stone.draw(screen, sprites)

    def draw_tomb_dirt_rocks(self, screen: pygame.Surface, sprites: SpriteMap):
        self.__tomb_dirt_rocks[0].draw(screen, sprites)
        self.__tomb_dirt_rocks[1].draw(screen, sprites)
