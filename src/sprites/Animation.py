from dataclasses import dataclass
from enum import Enum
import pygame

from sprites.SpriteMap import SpriteMap

class Direction(Enum):
    TOP_LEFT = 1
    TOP_CENTER = 2
    TOP_RIGHT = 3
    CENTER_LEFT = 4
    CENTER_CENTER = 5
    CENTER_RIGHT = 6
    BOTTOM_LEFT = 7
    BOTTOM_CENTER = 8
    BOTTOM_RIGHT = 9

@dataclass
class Animation:
    """Class for storing animation data"""

    sprite_idxes: list[int]  # A list of indexes into the sprite map
    should_loop: bool
    direction: Direction     # Where to draw the sprites from

    def get_size(self) -> int:
        return len(self.sprite_idxes)

    def get_sprite(self, idx: int, sprites: SpriteMap) -> pygame.Surface:
        size = self.get_size()
        if self.should_loop:
            return sprites[self.sprite_idxes[idx % size]]
        return sprites[self.sprite_idxes[min(idx, len(self.sprite_idxes) - 1)]]
