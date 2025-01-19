from constants import ZOMBIE_SPAWN_ANIMATION_IDXES
from sprites.Animatable import Animatable
from sprites.Animation import Animation

class NormalZombie(Animatable):
    SPAWN_ANIMATION = Animation(ZOMBIE_SPAWN_ANIMATION_IDXES, False)

    def __init__(self, *, fps: float = 60):
        self.set_fps(fps)

    def spawn(self, start_ms: float):
        self.set_animation(NormalZombie.SPAWN_ANIMATION, start_ms)
