from enum import Enum
from typing import Optional
from constants import ZOMBIE_SPAWN_ANIMATION_IDXES
from sprites.Animatable import Animatable
from sprites.Animation import Animation


class ZombieAnimation(Enum):
    Spawning = 0

class NormalZombie(Animatable):
    SPAWN_ANIMATION = Animation(ZOMBIE_SPAWN_ANIMATION_IDXES, False)

    __active_animation: Optional[ZombieAnimation]

    def __init__(self, *, fps: float = 60, x: float = 0, y: float = 0):
        self.set_fps(fps)
        self.set_pos(x, y)
        self.__active_animation = None

    def spawn(self, start_ms: float):
        self.set_animation(NormalZombie.SPAWN_ANIMATION, start_ms)
        self.__active_animation = ZombieAnimation.Spawning

    def get_active_animation(self) -> Optional[ZombieAnimation]:
        return self.__active_animation
