import pygame

from sprites.SpriteMap import SpriteMap


class Animation:
    """Class for storing animation data"""

    __sprite_idxes: list[int]  # A list of indexes into the sprite map
    __should_loop: bool

    def __init__(self, sprite_idxes: list[int], should_loop: bool):
        self.__sprite_idxes = sprite_idxes
        self.__should_loop = should_loop

    def get_size(self) -> int:
        return len(self.__sprite_idxes)

    def get_sprite(self, idx: int, sprites: SpriteMap) -> pygame.Surface:
        size = self.get_size()
        if self.__should_loop:
            return sprites[self.__sprite_idxes[idx % size]]
        return sprites[self.__sprite_idxes[min(idx, len(self.__sprite_idxes) - 1)]]

    def is_end(self, idx: int) -> bool:
        if self.__should_loop:
            return False
        return idx >= self.get_size()
