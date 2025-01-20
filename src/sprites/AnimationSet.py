from dataclasses import dataclass

import pygame

from sprites.Animation import Animation, Direction
from sprites.SpriteMap import SpriteMap

@dataclass
class AnimationSet:
    queue: list[Animation]
    fps: float

    def get_size(self) -> int:
        return sum([anim.get_size() for anim in self.queue])

    def get_sprite(self, idx: int, sprites: SpriteMap) -> tuple[pygame.Surface, Direction]:
        accumulated_sum = 0
        for anim in self.queue:
            if anim == self.queue[-1]:
                return (anim.get_sprite(idx - accumulated_sum, sprites), anim.direction)
            if anim.get_size() + accumulated_sum < idx:
                return (anim.get_sprite(idx - accumulated_sum, sprites), anim.direction)
            accumulated_sum += anim.get_size()
        raise Exception("Unreachable")
