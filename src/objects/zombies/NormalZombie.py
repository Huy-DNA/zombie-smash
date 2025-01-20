from constants import ZOMBIE_SPAWN_ANIMATION_IDXES
from sprites.Animatable import Animatable
from sprites.Animation import Animation, Direction
from sprites.AnimationSet import AnimationSet


SPAWN_ANIMATION = Animation(
    sprite_idxes=ZOMBIE_SPAWN_ANIMATION_IDXES,
    should_loop=False,
    direction=Direction.BOTTOM_CENTER,
)


class NormalZombie(Animatable):
    SPAWN_ANIMATION_SET = AnimationSet(queue=[SPAWN_ANIMATION], fps=60)

    def __init__(self, *, base_pos: tuple[float, float] = (0, 0)):
        self.set_base_pos(base_pos[0], base_pos[1])

    def spawn(self, *, start_ms: float = 0):
        self.set_animation_set(NormalZombie.SPAWN_ANIMATION_SET, start_ms=start_ms)
