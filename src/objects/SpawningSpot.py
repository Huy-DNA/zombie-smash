from typing import Optional

import pygame

from objects.Tomb import Tomb
from objects.zombies.NormalZombie import NormalZombie
from sprites.SpriteMap import SpriteMap


class SpawningSpot:
    __zombie: Optional[NormalZombie]
    __tomb: Tomb
    __base_pos: tuple[float, float]

    def __init__(self, *, base_pos: tuple[float, float]):
        self.__base_pos = base_pos
        self.__tomb = Tomb(base_pos=self.__get_tomb_pos())
        self.__zombie = None

    def __get_zombie_pos(self) -> tuple[float, float]:
        return (self.__base_pos[0] + 90, self.__base_pos[1] + 200)

    def __get_tomb_pos(self) -> tuple[float, float]:
        return self.__base_pos

    def has_zombie(self) -> bool:
        return self.__zombie is not None

    def get_zombie(self) -> Optional[NormalZombie]:
        return self.__zombie

    def spawn_zombie(self):
        self.__zombie = NormalZombie(base_pos=self.__get_zombie_pos())
        self.__zombie.spawn()

    def kill_zombie(self):
        self.__zombie = None

    def draw(self, screen: pygame.Surface, sprites: SpriteMap):
        self.__tomb.draw(screen, sprites)
        if self.__zombie:
            self.__zombie.draw(screen, sprites)
