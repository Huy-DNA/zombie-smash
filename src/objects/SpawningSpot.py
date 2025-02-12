from typing import Optional

import pygame

from objects.Tomb import Tomb
from objects.zombies.NormalZombie import NormalZombie
from sprites.SpriteMap import SpriteMap


class SpawningSpot:
    __base_pos: tuple[float, float]

    __active_zombie: Optional[NormalZombie]  # The alive zombie in this spot
    __transitioning_out_zombies: list[
        NormalZombie
    ]  # The zombies being killed or despawned
    __start_spawn_ms: Optional[float]  # The timestamp where the zombie last spawned

    __tomb: Tomb

    def __init__(self, *, base_pos: tuple[float, float]):
        self.__base_pos = base_pos

        self.__active_zombie = None
        self.__transitioning_out_zombies = []
        self.__start_spawn_ms = None

        self.__tomb = Tomb(base_pos=self.__get_tomb_pos())

    def __get_zombie_pos(self) -> tuple[float, float]:
        return (self.__base_pos[0] + 90, self.__base_pos[1] + 200)

    def __get_tomb_pos(self) -> tuple[float, float]:
        return self.__base_pos

    def __prune_transitioned_out_zombies(self):
        self.__transitioning_out_zombies = [
            zombie
            for zombie in self.__transitioning_out_zombies
            if not zombie.can_animation_end()
        ]

    def has_zombie(self) -> bool:
        self.__prune_transitioned_out_zombies()
        return (
            self.__active_zombie is not None
            or len(self.__transitioning_out_zombies) > 0
        )

    def get_spawned_time(self) -> float:
        if self.__start_spawn_ms is None:
            return 0
        return pygame.time.get_ticks() - self.__start_spawn_ms

    def get_active_zombie(self) -> Optional[NormalZombie]:
        return self.__active_zombie

    def spawn_zombie(self):
        self.__active_zombie = NormalZombie(base_pos=self.__get_zombie_pos())
        self.__active_zombie.spawn()
        self.__start_spawn_ms = pygame.time.get_ticks()

    def kill_zombie(self):
        self.__prune_transitioned_out_zombies()
        self.__start_spawn_ms = None
        if self.__active_zombie is None:
            return
        self.__active_zombie.kill()
        self.__transitioning_out_zombies.append(self.__active_zombie)
        self.__active_zombie = None

    def despawn_zombie(self):
        self.__start_spawn_ms = None
        if self.__active_zombie is None:
            return
        self.__active_zombie.despawn()
        self.__transitioning_out_zombies.append(self.__active_zombie)
        self.__active_zombie = None

    def draw(self, screen: pygame.Surface, sprites: SpriteMap):
        self.__tomb.draw(screen, sprites)
        if self.__active_zombie:
            self.__active_zombie.draw(screen, sprites)

        self.__prune_transitioned_out_zombies()
        for zombie in self.__transitioning_out_zombies:
            zombie.draw(screen, sprites)
